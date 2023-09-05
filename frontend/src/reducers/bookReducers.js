import {
    BOOK_LIST_REQUEST,
    BOOK_LIST_SUCCESS,
    BOOK_LIST_FAIL,
    BOOK_LIST_CLEARED,

    BOOK_DETAIL_REQUEST,
    BOOK_DETAIL_SUCCESS,
    BOOK_DETAIL_FAIL,

    BOOK_COVER_REQUEST,
    BOOK_COVER_SUCCESS,
    BOOK_COVER_FAIL,
} from "../Constants/bookConstants";

export const bookListReducer = (state = {books:[]}, action) => {
    switch(action.type){
        case BOOK_LIST_REQUEST:
            return {...state, loading: true, books:[]};

        case BOOK_LIST_SUCCESS:
            return {...state, loading: false, books: action.payload};
        
        case BOOK_LIST_FAIL:
            return {loading: false, error: action.payload};

        case BOOK_LIST_CLEARED:
            return {loading: false, books: action.payload};
        
        default:
            return state;
    }
} 


export const bookDetailReducer = (state = {book:[]}, action) => {
    switch(action.type){
        case BOOK_DETAIL_REQUEST:
            return {...state, loading: true};

        case BOOK_DETAIL_SUCCESS:
            return {...state, loading: false, book: action.payload};
        
        case BOOK_DETAIL_FAIL:
            return {loading: false, error: action.payload};
        
        default:
            return state;
    }
}


export const bookCoverReducer = (state = {}, action) => {
    switch(action.type){
        case BOOK_COVER_REQUEST:
            return {...state, loading: true};

        case BOOK_COVER_SUCCESS:
            return {...state, loading: false, isCover: true};
        
        case BOOK_COVER_FAIL:
            return {loading: false, isCover: false};
        
        default:
            return state;
    }
}


