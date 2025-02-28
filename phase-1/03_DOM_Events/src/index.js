function formatPrice(price) {
  return "$" + Number.parseFloat(price).toFixed(2);
}

//////////////////////////////////////
// render functions  (Data => Display)
//////////////////////////////////////

// create a function renderHeader() that takes the store name from bookStore and adds to the DOM
function renderHeader(bookStore) {
  document.querySelector("#store-name").textContent = bookStore.name;
}

function renderFooter(bookStore) {
  document.querySelector("#store").textContent = bookStore.location;
  document.querySelector("#number").textContent = bookStore.number;
  document.querySelector("#address").textContent = bookStore.address;
}

// function: renderBook(book)
// --------------------------
// accepts a book object as an argument and creates
// an li something like this:
// <li class="list-li">
//   <h3>Eloquent JavaScript</h3>
//   <p>Marjin Haverbeke</p>
//   <p>$10.00</p>
//   <img src="https://images-na.ssl-images-amazon.com/images/I/51IKycqTPUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg" alt="Eloquent JavaScript cover"/>
// </li>
// appends the li to the ul#book-list in the DOM
function renderBook(book) {
  const li = document.createElement("li");
  li.className = "list-li";

  const h3 = document.createElement("h3");
  h3.textContent = book.title;
  li.append(h3);

  const pAuthor = document.createElement("p");
  pAuthor.textContent = book.author;
  li.append(pAuthor);

  const pPrice = document.createElement("p");
  pPrice.textContent = formatPrice(book.price);
  li.append(pPrice);

  const img = document.createElement("img");
  img.src = book.imageUrl;
  img.alt = `${book.title} cover`;
  img.title = `${book.title} cover`;
  li.append(img);

  const btn = document.createElement("button");
  btn.textContent = "Delete";
  li.append(btn);

  btn.addEventListener("click", () => {
    li.remove();
  });

  document.querySelector("#book-list").append(li);
}

////////////////////////////////////////////
// call render functions to populate the DOM
////////////////////////////////////////////

renderHeader(bookStore);
renderFooter(bookStore);
bookStore.inventory.forEach(renderBook);

let isFormShowing = false;

const toggleButton = document.querySelector("#toggleForm");
const form = document.querySelector("#book-form");

function hideForm() {
  form.className = "collapsed";
  isFormShowing = false;
}

toggleButton.addEventListener("click", (e) => {
  if (isFormShowing) {
    hideForm();
  } else {
    form.className = "";
    isFormShowing = true;
  }
});

// form.addEventListener("submit", );

const handleSubmission = (e) => {
  e.preventDefault();
  const newBook = {
    title: e.target.title.value,
    author: e.target.author.value,
    price: e.target.price.value,
    reviews: [],
    inventory: e.target.inventory.value,
    imageUrl: e.target.imageUrl.value,
  };

  renderBook(newBook);

  e.target.reset();
  hideForm();
  const message = document.createElement("p");
  message.textContent = "New book submitted!";
  document.querySelector("#form-wrapper").append(message);
  setTimeout(() => {
    message.remove();
  }, 2000);
};

const fav = { "favorite-color": "blue" };
const second = { favoriteColor: "blue" };

fav["favorite-color"];

second.favoriteColor;