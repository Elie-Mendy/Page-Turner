import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Row, Col, Button, Card, ListGroup } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../Components/Loader";
import Message from "../Components/Message";
import ProfileBanner from '../Components/ProfileBanner';
import ProfilMenu from '../Components/ProfilMenu';
import ProfilAbout from '../Components/ProfilAbout'
import ProfilPost from '../Components/ProfilPost'
import BlogPost from '../Components/BlogPost'
import Post from '../Components/Post'



import { getUserDetails, updateUserProfile } from "../actions/userActions";
import { USER_UPDATE_PROFILE_RESET } from '../constants/userConstants'

function ProfileScreen() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [message, setMessage] = useState("");

    const navigate = useNavigate();
    const dispatch = useDispatch();

    const userDetails = useSelector((state) => state.userDetails);
    const { error, loading, user } = userDetails;

    const userLogin = useSelector((state) => state.userLogin);
    const { userInfo } = userLogin;

    const userUpdateProfile = useSelector((state) => state.userUpdateProfile);
    const { success } = userUpdateProfile;

    useEffect(() => {
        if (!userInfo) {
            navigate('/login');
        } else {
            if(!user || !user.name || success){
                dispatch(getUserDetails('profile'))
                dispatch({ type: USER_UPDATE_PROFILE_RESET })
            } else {
                setName(user.name)
                setEmail(user.email)
            }
        }
    }, [dispatch, navigate, userInfo, user, success]);

    const submitHandler = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            setMessage("Password do not match");
        } else {
            setMessage("");
            dispatch(updateUserProfile({
                'id': user._id,
                'name': name,
                'email': email,
                'password': password,
            }))
        }
    };

    return (
        <>
            <ProfileBanner/>
            <ProfilMenu/>
            <Row>
                <Col md={3}>
                    <ProfilAbout/>
                </Col>
                <Col md={9}>
                    <ListGroup variant="flush">
                        <ListGroup.Item>
                            <BlogPost/>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <ProfilPost/>
                            <ProfilPost/>
                            <ProfilPost/>
                            <ProfilPost/>
                            <ProfilPost/>
                            <ProfilPost/>
                        </ListGroup.Item>
                    </ListGroup>
                </Col>
            </Row>
        </>
    );
}

export default ProfileScreen;
