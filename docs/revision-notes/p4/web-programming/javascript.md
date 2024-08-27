---
title: Javascript
---

This note is mainly based on this video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/hdI2bqOjy3c?si=9EdJqrZ0bP_Nm4WW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Introduction

For documentation about something, just google for: `<query> MDN` - MDN is Mozilla Developer Network, or, you can also search like: `<query> w3schools` - W3Schools is also another great site.

Javascript is not statically typed. TypeScript lets us do this (kinda like `mypy` for python) - but we won't be discussing it here.

## Comments

```js
// single line comment

/*  
    this is a
    multi line
    comment
*/
```


## Showing Stuff

```js
// show the alert on top of the DOM (not in DOM)
alert("Message goes here");

// show to console (dev tools)
console.log("txt");     // grey
console.warn("txt");    // yellow
console.error("txt");   // red
```


## Variables

```js
// declare the variable
// by default, will have the value: `undefined`
var x;

// initialize the varible with a value
x = 5;
```

### `var`

```js
// scope: global
// avialable to all blocks

var x = 5;      // declare and 
                // initialize the variable

x = 10;         // re-assigen a value

console.log(x); // 10
```

### `let`

```js
// scope: current block only
// similiar to `var`, but different scope
```

### `const`

```js
// scope: global
// immutable (cannot be directly re-assigned)

const x = 5;    // declare and 
                // initialize the constant

x = 10;         // re-assign it
                // this fails, and 
                // a TypeError will be raised

console.log(x); // this won't run because the script
                // will stop at `x = 30;`
```


## Data Types

```js
// String
// ---
// can use single strings or double strings
// Template strings - in the concatenation section (`hi ${x} `) 
// ---
const name = 'Hello';
// ---
console.log( typeof name ); // 'string'
console.log( name.length ); // 5
console.log( name.toUpperCase() ); // 'HELLO'
console.log( name.toLowerCase() ); // 'hello'
console.log( name.substring(0, 4) ); // 'Hell'
                                     // Upto character with 4th index (not inclusive)
                                     // 0: inclusive
                                     // 4: not inclusive (actually upto 3)
console.log( name.split('') ); // ['h', 'e', 'l', 'l', 'o']
console.log( name.split('ll') ); // ['he', 'o']
console.log( name.split('l') ); // ['he', '', 'o']

// --- 


// Number
// ---
// there is no seperate data type for decimal numbers
// and no seperate data type for integers
// ---
const x = 5; 
const y = 5.69; 
// ---
console.log(typeof x); // 'number'
console.log(typeof y); // 'number'
// ---


// Boolean
// ---
// uhh
// ---
const a = true;
// ---
console.log(typeof a); // 'boolean'
// ---


// null
// ---
// basically "nothing"
// ---
const z = null;
// ---
console.log(typeof z); // 'object'
// ---


// undefined
// ---
// can also make varaibles explicitly undefined
// un-initialized variables are undefined by default
// ---
let b = undefined;
// ---
console.log(typeof b); // 'undefined'
// ---

```


## Concatenation

```js
const name = 'Hirusha';
const age = 18;

// Concatenated
console.log("My name is " + name + "and I am " + age + "years old");

// Template Strings
// ` sign instead of ' or "
console.log(`My name is ${name} and I am ${age} years old`);
```

## Arrays

```js
// Variables that hold multiple values
// can hold any datatype (mixed) - like python
// index starts from 0 (for the first element)
// dynamic length (not fixed, like in Java)

// using a constructor
const n = new Array(1, 2, 3, 'hello', true);

// normal way
const n = [1, 2, 3, 'hello', true];

// is array?
console.log( Array.isArray(n) ); // true

console.log( typeof n ); // 'object'

// accessing elements using the index
console.log( n[0] );    // 1
console.log( n[1] );    // 2
console.log( n[2] );    // 3
console.log( n[3] );    // 'hello'
console.log( n[4] );    // true

// re-assigning values
n[1] = 'world';
console.log( n ); // [1, 'world', 3, 'hello', true]

// add to end
n.push('test'); 
console.log( n ); // [1, 'world', 3, 'hello', true, 'test']

// add to front
n.unshift(true);
console.log( n ); // [true, 1, 'world', 3, 'hello', true, 'test']

// remove last element
n.pop();          // 'test'
console.log( n ); // [true, 1, 'world', 3, 'hello', true]

// note that the list has two elements with the same value
// it's `true` at index 0 and index 5
console.log( n.indexOf(true) ); // 0
// note that this only returns the index of the first element
//      if the element's value is repeated 
```

## Object Literals

### Basics

```js
// Basically key-value pairs, like JSON (NOT JSON)

// declaring and initializing values
const person = {
    f_name: 'John',
    l_name: 'Doe',
    age: 10,
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: '69 main street',
        city: 'Town',
        state: 'Test'
    }
}

console.log( person ); // { ... }
console.log( person.f_name ); // 'John'
console.log( person.hobbies[1] ); // 'movies'
console.log( person.address.city ); // 'Town'
console.log( typeof person ); // 'object'

const { f_name, l_name, address: { city } } = person;
console.log( f_name ); // 'John'
console.log( l_name ); // 'Doe'
console.log( city ); // 'Town'

person.email = 'johndoe@email.com';
console.log( person ); // { ..., email, ... }
```

### Using Arrays

```js
// an array of object literals
const todos = [
    {
        id: 1,
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id: 2,
        text: 'Meeting with boss',
        isCompleted: true
    },
    {
        id: 3,
        text: 'Dentist appointment',
        isCompleted: false
    },
]

console.log( todos ); // [{...}, {...}, {...}]
console.log( todos[1].text ); // 'Meeting with boss'
console.log( typeof todos ); // 'object'
```

### Converting to JSON

```js
const todos = [
    {
        id: 1,
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id: 2,
        text: 'Meeting with boss',
        isCompleted: true
    }
]

console.log( todos ); // [{...}, {...}]
console.log( typeof todos ); // 'object'\


// convert to JSON stringify)
const todosJSON = JSON.stringify(todos);

console.log( todosJSON );
/*
[
    {"id":1,"text":"Take out trash","isCompleted":true},
    {"id":2,"text":"Meeting with boss","isCompleted":true}
]
*/
console.log( typeof todosJSON ); // 'string'
console.log( todosJSON[0] ); // '['
console.log( todosJSON[1] ); // '{'
console.log( todosJSON[2] ); // '"'
console.log( todosJSON[3] ); // 'i'
console.log( todosJSON[4] ); // 'd'
                             // literally a `string`
```

## For Loops

```js

// start counting from `0`
// while `i < 10`
// increment `i` by `1`
for (let i = 0; i < 10; i++) {
    console.log(i);
}
// 0 -> 9

for (let i = 0; i <= 10; i++) {
    console.log(i);
}
// 0 -> 10
```

## While Loops

```js

// start from 0
let i = 0;

// repeat while `i < 10`
while (i < 10) {
    console.log(i);
    i++;    // make sure to increment i
            // in a way such that the loop breaks
            // otherwise, its an infinite loop
}
// 0 -> 9

// repeat while `i <= 10`
while (i <= 10) {
    console.log(i);
    i++;    // make sure to increment i
            // in a way such that the loop breaks
            // otherwise, its an infinite loop
}
// 0 -> 10
```

## Iterating an Array

Iterating through an Array

```js
const todos = [
    {
        id: 1,
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id: 2,
        text: 'Meeting with boss',
        isCompleted: false
    }
]

// Using a for loop (old approach)
for (let i = 0; i < todos.length; i++) {
    console.log( todos[i].text );
}

// Using a for loop (new approach)
for (let todo of todos) {
    console.log( todo.text );
}

// using `.forEach` method (higher order)
// what get's passed in is called the 'callback function'
todos.forEach( 
    function (todo) {
        console.log(todo.text);
    } 
);

// using `.map` method
// we only select what we want
// an array will be returned (so, we store in a variable)
const todoText = todos.map(
    function (todo) {
        return todo.text;
    }
);
console.log(todoText); // ['Take out trash', 'Meeting with boss']


// using `.filter`
// we filter out the items using the given condition
//       mentioned inside the callback function
// an array will be returned (so, we store in a variable)
const todoCompleted = todos.filter(
    function (todo) {
        return todo.isCompleted === true;
    }
);
console.log(todoCompleted); // [ {id: 1, ...} ]

// Chaining these methods
const todoCompletexTexts = todos.filter(
    function (todo) {
        return todo.isCompleted === true;
    }
).map(
    function (todo) {
        return todo.text;
    }
);
console.log(todoCompleted); // ['Take out trash']
```

## Conditionals

### Normal Way

```js
// using '=='
var x = 10;
if (x == 10) {
    console.log('x is 10');     // this will run
}

// it will not care about datatype
var x = '10';
if (x == 10) {
    console.log('x is 10');     // this will run
}

// to also check the data type
// use '==='
var x = '10';
if (x === 10) {
    console.log('x is 10');     // this will NOT run
}

// else if & else (optional)
// can use as many `else if` as required
// always ends with `else`
var x = 10;
if (x > 10) {
    console.log('x is greater than 10');
} 
else if (x < 10) {
    console.log('x is less than 10');
}
else {
    console.log('x is equal to 10');    // this will run
}


var x = 4;
var y = 11;

// OR
if (x > 6 || y > 10 ) {
    console.log('atleast one condtion is met (OR)'); // this will run
        // because `y > 10` condition is met
} 

// AND
if (x > 6 && y > 10 ) {
    console.log('both conditions are met (AND)'); // this will NOT run
        // because `x > 6` (4 is not greater than 6) condition is NOT met
} 
```

### Other

```js
const x = 11;

// ternary Operator
// for quick one-liner if-else
const result = x > 10 ? 'True' : 'False'
console.log( result );  // 'True'
                        // 11 is greater than 10


// Swicth-Case
// can be used in Menus
switch (result) {
    case 'True':
        console.log('result was True');     // this will run
        break;
    case 'False':
        console.log('result was False');
        break;
    default:
        console.log('result was not True nor False')
        break;
}
```

## Functions

### Normal Functions

```js
var x;

// Just get stuff done
function addNum(n1, n2) {
    console.log(n1 + n2);
    // returns `undefined` by default
}
x = addNum(2, 3); // outputs: 5
console.log(x); // undefined
                // because nothing is being returned


// while getting stuff done,
// we can also return the answer
function addNum(n1, n2) {
    var ans = n1 + n2
    return ans;
}
x = addNum(2, 3);   // just runs the function
console.log(x);     // 5 


// default values to function arguments
//      they are the values that we pass in
function addNum(n1 = 2, n2 = 3) {
    console.log(n1 + n2);
}
addNum(); // 5
```

### Arrow Functions

```js

// `=>` is called the 'fat arrow'
const addNum = (n1 = 2, n2 = 3) => {
    let ans = n1 + n2;
    console.log(ans);
}
addNum();

// if we only have one expression for the function
// like lambda functions in python
const addNum = (n1 = 2, n2 = 3) => console.log(n1 + n2);

// or if we want to return it
// note that no 'return' keyword is being used
const addNum = (n1 = 2, n2 = 3) => n1 + n2;

// if we have one argument
const addFive = n1 => n1 + 5;
addFive(3); // returns: 8
```

### as Objects

```js
// constructor function
function Person(fName, lName, dob) {
    // properties
    this.fName = fName;
    this.lname = lName
    this.dob = new Date(dob)

    // methods
    this.getBirthYear = function () {
        return this.dob.getFullYear(); // for Date object
    }
};

// methods can be also defined outside of the main function
Person.prototype.getFullName = function () {
    return `${this.fName} ${this.lName}`;
}

// instantiate objects
const p1 = new Person('John', 'Doe', '4-3-1980');
const p2 = new Person('Jane', 'Doe', '3-6-1970');

console.log( p1.getBirthYear() ); // 1980
console.log( p1.getFullName() ); // 'John Doe'
```

## Classes

Object Oriented Programming stuff. This is the new way. Using that function is the old way.

Classes were introduced in ES6 (2015)

```js
// class
class Person {
    constructor (fName, lName, dob) {
        // properties
        this.fName = fName;
        this.lname = lName
        this.dob = new Date(dob)
    }

    // methods
    getBirthYear = function () {
        return this.dob.getFullYear(); // for Date object
    }
    getFullName = function () {
        return `${this.fName} ${this.lName}`;
    }
}
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```

## Comments

```js
```