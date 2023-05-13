import axios from "axios";
import {
    API_KEY,
    API_BOOKS_URL,
    BOOK_LIST_REQUEST,
    BOOK_LIST_SUCCESS,
    BOOK_LIST_FAIL,

    BOOK_DETAIL_REQUEST,
    BOOK_DETAIL_SUCCESS,
    BOOK_DETAIL_FAIL,

    BOOK_COVER_REQUEST,
    BOOK_COVER_SUCCESS,
    BOOK_COVER_FAIL,
} from "../Constants/bookConstants";

// redux-thunk allows us to return async function instead of regular actions
export const listBooks = (searchValue=null, searchType=null) => async (dispatch, isbn) => {
    try {
        dispatch({ type: BOOK_LIST_REQUEST });

        switch(searchType) {
            case "tab2":
                const recommandedData = await axios.get(/recommandation/)
                const isbns = recommandedData.data.stdout.split(', ');
                
                const requests = [];
                const recommandedBooks= {kind:"books#volumes", items:[]};
                for (let i = 0; i < isbns.length; i++) {
                    const url = `https://www.googleapis.com/books/v1/volumes?q=isbn:${isbns[i]}`;
                    requests.push(axios.get(url));
                }
                
                await axios.all(requests)
                .then(responses => {
                    // Les informations sur les livres se trouvent dans les objets responses[i].data.items[0].volumeInfo
                    for (let i = 0; i < responses.length; i++) {

                    console.log(responses[i].data.items[0]);
                    recommandedBooks.items.push(responses[i].data.items[0])
                    }
                })
                .catch(error => console.log(error));
                console.log(recommandedBooks)
                dispatch({
                    type: BOOK_LIST_SUCCESS,
                    payload: recommandedBooks,
                });
                break;
            default:
                let query = searchValue ? `intitle:${searchValue}` : 'subject:fantasy';
                const request = `${API_BOOKS_URL}/volumes?q=${query}&orderBy=newest&caseInsensitive=true&maxResults=40` 
    
                const { data } = await axios.get(request)
                console.log('data : ', data)
                dispatch({
                    type: BOOK_LIST_SUCCESS,
                    payload: data,
                });
                break;
        }
    } catch (error) {
        dispatch({
            type: BOOK_LIST_FAIL,
            payload: error.message,
        });
    }
};

export const listBooksDetails = (isbn) => async (dispatch) => {
    try {
        dispatch({type : BOOK_DETAIL_REQUEST});

        // const request = `${API_BOOKS_URL}/volumes?q=isbn:${isbn}&key=${API_KEY}&maxResults=40`;
        const request = `${API_BOOKS_URL}/volumes?q=isbn:${isbn}&maxResults=40`;

        const { data } = await axios.get(request)
        dispatch({
            type: BOOK_DETAIL_SUCCESS,
            payload: data.items[0]
        })

    } catch (error) {
        dispatch({
            type: BOOK_DETAIL_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }

    
    
}

export const getCoverFromIsbn = (isbn) => async (dispatch) => {
    try {
        //await axios.get(`https://covers.openlibrary.org/b/id/${isbn}-M.jpg?default=false`)
        let img = new Image();
        img = await axios.get (`http://images.amazon.com/images/P/${isbn}.01.LZZZZZZZ.jpg`)
       
        if (img.data !== "GIF89a\u0001\u0000\u0001\u0000�\u0001\u0000\u0000\u0000\u0000���!�\u0004\u0001\u0000\u0000\u0001\u0000,\u0000\u0000\u0000\u0000\u0001\u0000\u0001\u0000\u0000\u0002\u0002L\u0001\u0000;") {
            dispatch({ type: BOOK_COVER_SUCCESS })
        } else {
            dispatch({ type: BOOK_COVER_FAIL })
        }
        

    } catch (error) {
        dispatch({ type: BOOK_COVER_FAIL })
    } 
    
}