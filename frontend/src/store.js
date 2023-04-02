import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from "redux-thunk"; // midleware for returning an 
import { composeWithDevTools } from "redux-devtools-extension";

import { productListReducer, productDetailReducer } from "./reducers/productReducers";
import { cartReducer } from "./reducers/cartReducers";
import { userLoginReducer , userRegisterReducer, userDetailsReducer } from "./reducers/userReducer"

const reducer = combineReducers({
    productList: productListReducer,
    productDetail: productDetailReducer,
    cart: cartReducer,
    userLogin: userLoginReducer,
    userRegister: userRegisterReducer,
    userDetails: userDetailsReducer,
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