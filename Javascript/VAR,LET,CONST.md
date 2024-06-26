__var,let,const__

console.log(myConst1); // Output: ReferenceError: Cannot access 'myConst1' before initialization
let myConst1 = 42;

console.log(myConst2); // Output: ReferenceError: Cannot access 'myConst2' before initialization
const myConst2 = 42;

console.log(myConst3); // Output: undefined
var myConst3 = 42;


The main differences between `let`, `const`, and `var` in JavaScript are related to their scope, hoisting behavior, and mutability. Here's a summary:

**Scope**
   - `var`: Variables declared with `var` have function scope or global scope, meaning they are accessible throughout the function in which they are declared (if declared inside a function) or throughout the entire script (if declared outside any function).
   - `let` and `const`: Variables declared with `let` and `const` have block scope, meaning they are only accessible within the block in which they are declared, such as a loop, conditional statement, or function.

2. **Hoisting**:
   - `var`: Variable declarations using `var` are hoisted to the top of their containing function or global scope during compilation, but their assignments are not hoisted. This means you can access the variable before it's declared, but its value will be `undefined`.
   - `let` and `const`: Variable declarations using `let` and `const` are hoisted to the top of their containing block, but they are not initialized. This means you cannot access the variable before it's declared, resulting in a ReferenceError.

3. **Reassignment**:
   - `var`: Variables declared with `var` can be reassigned and updated.
   - `let`: Variables declared with `let` can be reassigned but not re-declared within the same scope.
   - `const`: Variables declared with `const` cannot be reassigned or re-declared. However, if the variable is an object or array, its properties or elements can still be modified.

4. **Mutability**:
   - `var` and `let`: Variables declared with `var` or `let` can be mutable or immutable, depending on how they are used.
   - `const`: Variables declared with `const` are immutable, meaning they cannot be reassigned. However, if the variable is an object or array, its properties or elements can still be modified.

In summary, `var` has function or global scope, is hoisted with its declaration but not its initialization, and can be reassigned and re-declared. `let` and `const` have block scope, are hoisted without initialization, and have different rules regarding reassignment and mutability, with `const` being immutable. Using `let` and `const` can help avoid some of the issues associated with hoisting and provide better control over variable scoping and mutability in JavaScript code.

Variables declared with var:
var variables can be reassigned and updated, and they can also be re-declared within the same scope:

var varExample = "Initial value";
console.log(varExample); // Output: Initial value

var varExample = "Updated value"; // Redeclaration is allowed
console.log(varExample); // Output: Updated value

varExample = "Modified value"; // Reassignment is allowed
console.log(varExample); // Output: Modified value

Variables declared with let:
let variables can be reassigned but not re-declared within the same scope:

let letExample = "Initial value";
console.log(letExample); // Output: Initial value

// let letExample = "Updated value"; // Error: Identifier 'letExample' has already been declared
// Attempting to re-declare letExample in the same scope results in an error

letExample = "Modified value"; // Reassignment is allowed
console.log(letExample); // Output: Modified value

Variables declared with const:

const variables cannot be reassigned or re-declared. However, if the variable is an object or array, its properties or elements can still be modified:

const constExample = "Initial value";
console.log(constExample); // Output: Initial value

// const constExample = "Updated value"; // Error: Identifier 'constExample' has already been declared
// Attempting to re-declare constExample in the same scope results in an error

// constExample = "Modified value"; // Error: Assignment to constant variable
// Attempting to reassign constExample results in an error

const obj = { key: "value" };
obj.key = "modified value"; // Modifying properties of const object is allowed
console.log(obj); // Output: { key: "modified value" }
In the const example, while the variable itself cannot be reassigned or re-declared, we can still modify its properties because the variable holds a reference to an object, and the reference remains constant. This allows for mutation of the object's properties or elements. However, reassigning the variable itself (e.g., constExample = "Modified value";) is not allowed.



var declarations:
Hoisted to the top of their function or global scope during compilation.
Initialized with undefined by default even before their declaration statement is encountered.
let and const declarations:
Hoisted to the top of their block scope during compilation.
Not initialized until their declaration statement is encountered in the code.
Accessing them before their declaration results in a ReferenceError.
So, while let and const declarations are hoisted to the top of their block scope like var declarations, they differ in terms of initialization behavior and temporal dead zone (TDZ) restrictions, making them behave differently in certain situations.
