import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import ProfileBanner from "../Components/ProfileBanner";
import ProfilMenu from "../Components/ProfilMenu";

import { getUserDetails, updateUserProfile } from "../Actions/userActions";
import { USER_UPDATE_PROFILE_RESET } from "../Constants/userConstants";

function ProfileScreen() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
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
            navigate("/login");
        } else {
            if (!user || !user.name || success) {
                dispatch(getUserDetails("profile"));
                dispatch({ type: USER_UPDATE_PROFILE_RESET });
            } else {
                setName(user.name);
                setEmail(user.email);
            }
        }
    }, [dispatch, navigate, userInfo, user, success]);

    return (
        <>
            <ProfileBanner />
            <ProfilMenu />
        </>
    );
}

export default ProfileScreen;
