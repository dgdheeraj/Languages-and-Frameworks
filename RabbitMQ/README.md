# RabbitMQ

## What is it?
It is an open-source message broker that implements Advanced Message Queuing Protocol (AMQP). It cannot do any kind of batch processing. Only stream since it considers each message individually.

## Why is it required?
RabbitMQ allows different applications to communicate with each other by sending and receiving messages asynchronously. It acts as an intermediary or middleman that facilitates communication between various components of a distributed system. This can include different parts of an application, different applications, or different systems altogether.

Assume you have a dB that takes caters requests. Now, its load increases, and at some point it may crash. Having an intermediate service like RabbitMQ can help in managing the load to the dB and keep a copy of requests in case the dB crashes.


## Alternatives
- Apache Kafka: A Kafka cluster provides high-throughput stream event processing with a more complex architecture

You can think of RabbitMQ as a post office that receives mail and delivers it to the intended recipients. Meanwhile, Kafka is similar to a library, which organizes messages on shelves with different genres that producers publish. Then, consumers read the messages from the respective shelves and remember what they have read

## 1. "Hello World!"
- Producing means nothing more than sending. A program that sends messages is a producer
- A queue is the name for the post box in RabbitMQ. Although messages flow through RabbitMQ and your applications, they can only be stored inside a queue. A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.
- Consuming has a similar meaning to receiving. A consumer is a program that mostly waits to receive messages

```
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
```

### Sending
Create a queue called `hello`
```
channel.queue_declare(queue='hello')
```

Default exchange is `''`, in this exchange you can route the messgage to the queue you want using `routing key`. 
```
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
```
### Receiving

The next step, just like before, is to make sure that the queue exists. Creating a queue using `queue_declare` is idempotent ‒ we can run the command as many times as we like, and only one will be created
```
channel.queue_declare(queue='hello')
```

Next, we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue
```
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback_function)

channel.start_consuming()
```

## 2. Work Queues

### Sending
```
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
```

### Receiving (Round-robin dispatching)
One of the advantages of using a Task Queue is the ability to easily parallelise work. If we are building up a backlog of work, we can just add more workers and that way, scale easily.

Doing a task can take a few seconds, you may wonder what happens if a consumer starts a long task and it terminates before it completes. With our current code once RabbitMQ delivers message to the consumer, it immediately marks it for deletion. In this case, if you terminate a worker, the message it was just processing is lost. The messages that were dispatched to this particular worker but were not yet handled are also lost.

In order to make sure a message is never lost, RabbitMQ supports message acknowledgments

```
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.') )
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='hello', on_message_callback=callback)
```

#### Persistence
To make the queue durable in case the RabbitMQ Service shuts down and restarts
```
channel.queue_declare(queue='hello', durable=True)
```

Now we need to mark our messages as persistent - by supplying a `delivery_mode` property with the value of `pika.DeliveryMode.Persistent`
```
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = pika.DeliveryMode.Persistent
                      ))
```

#### Fair Dispatch
RabbitMQ will only dispatch messages in the round robin fashion. It will not see the number of unacknowledged messages by the consumers. In order to defeat that we can use the Channel#basic_qos channel method with the prefetch_count=1 setting. This uses the basic.qos protocol method to tell RabbitMQ not to give more than one message to a worker at a time

```
channel.basic_qos(prefetch_count=1)
```

## 3. Publish/Subscribe
we'll deliver a message to multiple consumers. This pattern is known as "publish/subscribe".

### Exchanges

Producer never directly sends any message to a queue. It will always send it to an exchange. An exchange is very simple. It just takes messages from producers and pushes them to queues. The exchange must know what to do with the message, send it to a particular queue, or to many queues or discard it.
Exchange will never store any message. It will always forward it.
There are a few exchange types available: `direct`, `topic`, `headers` and `fanout`

Create a fanout exchange. The fanout exchange is very simple. As you can probably guess from the name, it just broadcasts all the messages it receives to all the queues it knows. And that's exactly what we need for our logger.
```
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
```

publish to the named exchange
```
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
```

Creating temporary queues
- once the consumer connection is closed, the queue should be deleted. There's an exclusive flag for that
- Providing empty names makes rabbitMQ name the queue to some random name
```
result = channel.queue_declare(queue='', exclusive=True)
```

Bind the queue to the exchange
```
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)
```

Overall Flow
- Producer creates an exchange and pushes messages to this exchange
- Consumer creates a queue and binds this queue to the exchange. 
- The exchange will push the message to queues that are binded to the exchange. 

## 6. RPC

Client Interface
```
fibonacci_rpc = FibonacciRpcClient()
result = fibonacci_rpc.call(4)
print(f"fib(4) is {result}")
```

A client sends a request message and a server replies with a response message. In order to receive a response the client needs to send a `callback` queue address with the request
```
result = channel.queue_declare(queue='', exclusive=True)
callback_queue = result.method.queue

channel.basic_publish(exchange='',
                      routing_key='rpc_queue',
                      properties=pika.BasicProperties(
                            reply_to = callback_queue,
                            ),
                      body=request)

# ... and some code to read a response message from the callback_queue ...
```

Creating a new queue for every RPC request is inefficient. Instead, we can create a single callback queue per client. Usage of `correlation_id` helps identify and match a response with a request. 

# References
- [RabbitMQ](https://www.rabbitmq.com/)
- [AWS RabbitMQ vs Kafka](https://aws.amazon.com/compare/the-difference-between-rabbitmq-and-kafka/)