import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Row, Col, Button, Card } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../Components/Loader";
import Message from "../Components/Message";
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
        <Row>
            <div>
                Thème
                <Row>
                    <Col md={1}>Image</Col>
                    <Col md={1}>Nom</Col>
                </Row>
            </div>
            <hr></hr>
            <Col md={4}>
                <h2>Profile</h2>
                <Row>
                    <h6>Lecture(s) en cours</h6>
                </Row>
                <br></br>
                <Row>
                    <Col md={4}><h6>Friends</h6></Col>
                    <Col md={4}><h6>Followers</h6></Col>
                    <Col md={4}><h6>Following</h6></Col>
                </Row>
                <br></br>
                <br></br>
                <div>
                    <h4>A propos</h4>
                    <Row>Description</Row>
                    <Row>Habite à / Pays</Row>
                </div>
                <br></br>
                <br></br>
                <div>
                    <h4>Social</h4>
                    <Row>Blog</Row>
                    <Row>Facebook</Row>
                    <Row>Instagram</Row>
                    <Row>Tiktok</Row>
                </div>
            </Col>
            <Col md={8}>
                <h2>Fil</h2>
                <div>
                    <Row><h4>Créer Post</h4></Row>
                </div>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <div>
                    <Row><h4>Anciens Posts</h4></Row>
                </div>
            </Col>
        </Row>
    );
}

export default ProfileScreen;
