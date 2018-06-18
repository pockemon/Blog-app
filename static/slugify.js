//grab the title and slug field
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

/* slugify the user input according to mentioned steps in function.
   slugify will be equal to a function which will take a parameter val.
   This val be a value which user enters in the title field.
*/
const slugify = (val) => {

    /*
     return the slugified version of string
     tostring will convert it in string if not
     tolowercase will convert all characters in lowercase
     trim is for removing white spaces
     regex for certain characters
     /g is for global
    */
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-') // Replace & with '-and-'
        .replace(/[\s\W-]+/g, '-') // Replace spaces, non-word characters and dashes with a single dash (-)

};

/* add an event listener to title field
   The event which we want to listen is the keyup event.
   The keyup event is when user presses a key on title field.
   If that event occurs we are going to fire a callback function which takes 
      the arrow function as an event.
*/
titleInput.addEventListener('keyup', (e) => {
    /*
      every time when keyup event happens it will take the input in title field,will apply the slugify function on that input and will set the value
      of variable 'value' to the value returned by that function
    */
    slugInput.setAttribute('value', slugify(titleInput.value));
});