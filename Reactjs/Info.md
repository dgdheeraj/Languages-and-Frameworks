Based on [React JS Tutorial for Beginners](https://www.youtube.com/watch?v=Ke90Tje7VS0)

## What is React?
JS library for fast and interactive UI

Components -> Pieces of UI 

Tree -> Starts with Root Component

Each component has a state and render function (descrives how it looks like)
Output of render() is a react element -> Simple Plain JS obj that maps to a DOM element, its not a real DOM element
its just a plain JS object that represents the DOM element in memeory.
React maintains a lightweight representation of DOM in memory which is referred to virtual DOM.
This virtual DOM is cheap to create. 
On changing state of component, we get a new react element. React will compare this element and its children 
with the previous one, figures out what has changed, and changes what's different.

## React vs Angular
Both are similar -> in terms of a component based architecture
However, Angular is a framework that is a complete solution, while React is only a view library to make sure the view is in sync with the state. 


## To create new react application (Windows 11)
`npx create-react-app name_of_the_app`
This command installs a lightweight development server, webpack for bundling our code, babel for compiling JS code and other tools. Zero config setup

Components returns JS object which is written in JSX (JavaScript XML)

Babel (a JS Compiler) converts this JSX to JS code that browsers can understand

## Prop vs State
Prop is the data that we pass to child components
State is the state of the component (internal)
Prop is read only

## Lifecycle

There are functions that can be used in each of the stages in class components, but for functional components, useEffect is used to mimic it
- Mount - When instance of component is created and inserted into DOM. Happens only once ('initial render')
```
const MyComponent = () => {
  useEffect(() => {
    // Code here runs after the component mounts
    console.log('ComponentDidMount');
    
    // Cleanup function (optional)
    return () => {
      console.log('ComponentWillUnmount');
      // Code here runs when the component is unmounted
    };
  }, []); // Empty dependency array means this effect runs once (on mount)
  
  return <div>My Component</div>;
};
```
    
- Update - when the component updates or re-renders. This reaction is triggered when the props are updated or when the state is updated. This phase can occur multiple times, which is kind of the point of React.
```
const MyComponent = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // Code here runs whenever count changes
    console.log('ComponentDidUpdate');

    // Cleanup function (optional)
    return () => {
      console.log('Clean up on count change');
    };
  }, [count]); // Effect runs whenever count changes
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};
```

- Unmount - when the component is removed from the DOM
```
const MyComponent = () => {
  useEffect(() => {
    console.log('ComponentDidMount');

    // Cleanup function (equivalent to componentWillUnmount)
    return () => {
      console.log('ComponentWillUnmount');
      // Code here runs when the component is unmounted
    };
  }, []);

  return <div>My Component</div>;
};
```
