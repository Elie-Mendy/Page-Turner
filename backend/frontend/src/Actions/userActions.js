import axios from 'axios';
import { 
    USER_LOGIN_REQUEST,
    USER_LOGIN_SUCCESS,
    USER_LOGIN_FAIL,

    USER_LOGOUT,

    USER_REGISTER_REQUEST,
    USER_REGISTER_SUCCESS,
    USER_REGISTER_FAIL,

    USER_DETAILS_REQUEST,
    USER_DETAILS_SUCCESS,
    USER_DETAILS_FAIL,
    USER_DETAILS_RESET,

    USER_UPDATE_PROFILE_REQUEST,
    USER_UPDATE_PROFILE_SUCCESS,
    USER_UPDATE_PROFILE_FAIL,
} from '../Constants/userConstants'


// redux-thunk allows us to return async function instead of regular actions 
export const login = (email, password) => async (dispatch) => {
    try {
        // dispatch the LOGIN RESUEST action 
        dispatch({type : USER_LOGIN_REQUEST});

        // Set and Launch a request
        const config = {
            headers: {
                'Content-type': 'application/json'
            }
        }

        const { data } = await axios.post(
            '/api/users/login/',
            {'username': email, 'password': password},
            config
        );
        
        // If the request successed,
        // Dispatch the LOGIN SUCCESS action 
        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })

        // Store data from the localStorage
        localStorage.setItem('userInfo', JSON.stringify(data))

    } catch (error) {
        dispatch({
            type: USER_LOGIN_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
    
}


export const logout = () => (dispatch) => {
    // Remove data from the localStorage
    localStorage.removeItem('userInfo')
    dispatch({ type: USER_DETAILS_RESET })
    dispatch({ type: USER_LOGOUT })
}


export const register = (name, email, password) => async (dispatch) => {
    try {
        // dispatch the LOGIN RESUEST action 
        dispatch({type : USER_REGISTER_REQUEST});

        // Set and Launch a request
        const config = {headers: {'Content-type': 'application/json'}}
        const { data } = await axios.post('/api/users/register/',
        { 'name': name, 'email': email, 'password': password },config)

        // If the request succeed,
        // Dispatch the REGISTER SUCCESS action 
        dispatch({
            type: USER_REGISTER_SUCCESS,
            payload: data
        })

        // If the previous request succeed,
        // Dispatch the LOGIN SUCCESS action 
        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })
        // Store data from the localStorage
        localStorage.setItem('userInfo', JSON.stringify(data))

    } catch (error) {
        dispatch({
            type: USER_REGISTER_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const getUserDetails = (id) => async (dispatch, getState) => {
    try {
        // dispatch the LOGIN RESUEST action 
        dispatch({type : USER_DETAILS_REQUEST});
        
        // get the user from our redux store
        const { userLogin: { userInfo } } = getState()

        // setting and launch the request 
        const { data } = await axios
        .create({
          headers: {
            Authorization: `Bearer ${userInfo.token}`,
            'Content-Type': 'application/json',
          },
        })
        .get(`/api/users/${id}/`)

        // If the request succeed,
        // Dispatch the REGISTER SUCCESS action 
        dispatch({
            type: USER_DETAILS_SUCCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: USER_DETAILS_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}


export const updateUserProfile = (user) => async (dispatch, getState) => {
    try {
        // dispatch the LOGIN RESUEST action 
        dispatch({type : USER_UPDATE_PROFILE_REQUEST});
        
        // get the user from our redux store
        const { userLogin: { userInfo } } = getState()

        // setting and launch the request 
        const { data } = await axios
        .create({
          headers: {
            Authorization: `Bearer ${userInfo.token}`,
            'Content-Type': 'application/json',
          },
        })
        .put(`/api/users/profile/update/`, user)

        // If the request succeed,
        // Dispatch the REGISTER SUCCESS action 
        dispatch({
            type: USER_UPDATE_PROFILE_SUCCESS,
            payload: data
        })

        // If the previous request succeed,
        // Dispatch the LOGIN SUCCESS action 
        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })
        // Store data from the localStorage
        localStorage.setItem('userInfo', JSON.stringify(data))


    } catch (error) {
        dispatch({
            type: USER_UPDATE_PROFILE_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}