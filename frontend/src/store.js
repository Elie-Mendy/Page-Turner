import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from "redux-thunk"; // midleware for returning an 
import { composeWithDevTools } from "redux-devtools-extension";

import { userLoginReducer , userRegisterReducer, userDetailsReducer, userUpdateProfileReducer } from "./reducers/userReducer"
import { bookListReducer, bookDetailReducer , bookCoverReducer } from "./reducers/bookReducers";


const reducer = combineReducers({
    userLogin: userLoginReducer,
    userRegister: userRegisterReducer,
    userDetails: userDetailsReducer,
    userUpdateProfile: userUpdateProfileReducer,
    bookList: bookListReducer,
    bookDetail: bookDetailReducer,
    bookCover: bookCoverReducer,
});

// Fetch data from the localStorage
const userInfoFromStorage = localStorage.getItem('userInfo') ? 
    JSON.parse(localStorage.getItem('userInfo')) : null

const cartItemsFromStorage = localStorage.getItem('cartItems') ? 
    JSON.parse(localStorage.getItem('cartItems')) : []

// Initialise State with the cart data
const initialState = {
    userLogin: { userInfo : userInfoFromStorage},
    cart: { cartItems: cartItemsFromStorage },
};

const middleware = [thunk];

const store = createStore(
    reducer, 
    initialState, 
    composeWithDevTools(applyMiddleware(...middleware))
);

export default(store);