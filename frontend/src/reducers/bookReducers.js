import {
    BOOK_LIST_REQUEST,
    BOOK_LIST_SUCCESS,
    BOOK_LIST_FAIL,
} from "../constants/bookConstants";

const initialState = {
    books: [],
    loading: false,
    error: null
  };

export const bookListReducer = (state = initialState, action) => {
    switch(action.type){
        case BOOK_LIST_REQUEST:
            return {...state, loading: true, books:[]};

        case BOOK_LIST_SUCCESS:
            return {...state, loading: false, books: action.payload};
        
        case BOOK_LIST_FAIL:
            return {loading: false, error: action.payload};
        
        default:
            return state;
    }
} 


