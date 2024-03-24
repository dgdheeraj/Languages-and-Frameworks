# AWS

## EC2 
Elastic Compute Cloud
- Provides scalable computing capacity on the AWS Cloud. 
- Basically Provides Virtual Machines 
- SSH to access the VM (VM stores user's public key and the private key is with the user. This is used to perform authentication and verify the user)

## Elastic Load Balancing

- Automatically distributes incoming traffic across multiple targets such as EC2 Instances, containers, IP Addresses.
- Monitors health of the targets and routes traffic only to the healthy targets.
- Types of ELB
    - Classic Load Balancer: Operates on request level and connection level, doesn't support features like host-based or path-based routing
    - Application Load Balancer: Specifically designed for web-applications with HTTP and HTTPS traffic. This works in the Application layer of the OSI Model. Also provides host-based and path-based routing.
        - Host Based Routing: Example usage would be routing requests between two sites like `medium.com` and `admin.medium.com`. 
        - Path Based Routing: Suppose website is `payzello.com` and company blog is `payzello.com/blog`, using ALB, we can route traffic based on path of the request(either `/` or `/blog`)
    - Network Load Balancer

### Creating ALB
Suppose you want to redirect traffic based on the path `/` and `/blog`
- Launch two EC2 instances, add a tag with key:Name, Value:Main and key:Name, Value:Blog
- Install apache web server on both the instances
- Create Two Target Groups
    - A target group allows you to tell the load balancer which protocol and port will receive the traffic on the registered instances.
    - Name each of the target groups as Main and Blog.
    - Navigate to the Targets tab, click on Edit, select the appropriate instance (`Main` instance for `Main` target group and `Blog` instance for `Blog` target group), click Add to registered and click Save.
- Create Load Balancer from the UI (Choose Application Load Balancer)
- Assign the ALB to the same security group as the two instances
- In Target groups, select the existing target group. In the name select Main and click Next. And click Create
- Select the Listeners tab and Click on View/edit rules.
- Click the + sign at the top to add a rule. In Add Condition select “Path is” and type /blog.
- Then in Add Action select Forward to and select Blog and then click Save.

## S3

Stands for Simple Storage Service
- It's an object storage service that provides scalability, availability, security and performance. 
- Stores data as objects within buckets. `Object` is a file and metadata that describes the files. `Bucket` is a container for objects.
- You create a bucket, specify name and region. Then you upload data to that bucket as objects in Amazon S3. Each object has a ket which is the unique identifier for object in the bucket. 
- S3 provides features like versioning. 
- S3 is strongly consistent ([Link Here for examples on concurrent applications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#:~:text=Concurrent%20applications))

NOTE: S3 can be considered as a key-value NOSQL Database (but it is definitely slow) 
[Link Here](https://stackoverflow.com/questions/56108144/using-s3-as-a-database-vs-database-e-g-mongodb#:~:text=You%20are%20%22-,considering%20using%20AWS%20S3%20bucket%20instead%20of%20a%20NoSQL%20database,-%22%2C%20but%20the%20fact)

## EBS
Elastic Beanstalk: Platform as a Service
- Assists in quickly deploying and managing applications in AWS Cloud without having to learn about the infrastructure that runs those applications. 
- EBS handles details of provisioning, load balancing, scaling and application health monitoring.
- You can also perform deployment tasks like changing size of the fleet of EC2 instances, or monitoring your application, directly from EBS Web interface.
- For Deploying Docker container using EBS
    - Make sure your image is available in Docker Hub
    - For source code origin, upload a json file specifying info about the container
    example: `Dockerrun.aws.json`
    ```
    {
    "AWSEBDockerrunVersion": "1",
    "Image": {
        "Name": "prakhar1989/catnip",
        "Update": "true"
    },
    "Ports": [
        {
        "ContainerPort": 5000,
        "HostPort": 8000
        }
    ],
    "Logging": "/var/log/nginx"
    }
    ```

## Lambda

- Compute Service that lets you run code without provisioning or managing servers.
- Only pass on your code, AWS Lambda takes care of everything else
- Lambda Use Case
    - File processing: Use Amazon Simple Storage Service (Amazon S3) to trigger Lambda data processing in real time after an upload.
    - Web applications: Combine Lambda with other AWS services to build powerful web applications that automatically scale up and down and run in a highly available configuration across multiple data centers.
    - IoT backends: Build serverless backends using Lambda to handle web, mobile, IoT, and third-party API requests.

Stages when setting up Lambda
- Download the code
- Start new execution environment
- Execute initialization code
- Execute handler code

`Cold Start` refers to the first two steps above where setup is taking place
After the execution completes, the execution environment is frozen. Lambda service retains the execution environment for a non-deterministic period of time for performance. During this time, if another request arrives for the same function, the service may reuse the environment. This second request typically finishes more quickly, since the execution environment already exists and it’s not necessary to download the code and run the initialization code. This is called a `warm start`.

## IAM
Identity and Access Management

## References
- [AWS EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [AWS ELB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [Hackernoon ELB](https://hackernoon.com/what-is-amazon-elastic-load-balancer-elb-16cdcedbd485)
- [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS EBS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [EBS Docker](https://docker-curriculum.com/#docker-on-aws)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [AWS Lambda Cold Start](https://docs.aws.amazon.com/lambda/latest/operatorguide/execution-environments.html)