import axios from "axios";
import {
    API_KEY,
    API_BOOKS_URL,
    BOOK_LIST_REQUEST,
    BOOK_LIST_SUCCESS,
    BOOK_LIST_FAIL,
} from "../constants/bookConstants";

// redux-thunk allows us to return async function instead of regular actions
export const listBooks = () => async (dispatch) => {
    try {
        dispatch({ type: BOOK_LIST_REQUEST });

        const { data } = await axios
            .create({
                headers: {
                    Authorization: `API Key ${API_KEY}`,
                    "Content-Type": "application/json",
                },
            })
            .get(`https://${API_BOOKS_URL}/volumes?q="haut royaume"`);

        dispatch({
            type: BOOK_LIST_SUCCESS,
            payload: data,
        });
    } catch (error) {
        dispatch({
            type: BOOK_LIST_FAIL,
            payload: error.message,
        });
    }
};
