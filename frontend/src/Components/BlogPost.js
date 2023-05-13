import { Row, Col } from "react-bootstrap";
import PostCard from "./PostCard";
import PostDetail from "./PostDetail";
import React, { useState, useEffect } from "react";
import axios from "axios";

function BlogPost() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get("/blog/").then((response) => {
            setData(response.data);
        });
    }, []);

    const [gridView, setGridView] = useState(true);
    const [postId, setpostId] = useState(1);

    return (
        <Row>
            {gridView ? (
                data.map((post, index) => (
                    <Col key={index} sm={12} md={6} lg={3}>
                        <PostCard
                            post={post}
                            setterView={setGridView}
                            setterPostId={setpostId}
                        />
                    </Col>
                ))
            ) : (
                <PostDetail
                    post={data.find((post) => post.id === postId)}
                    setterView={setGridView}
                />
            )}
        </Row>
    );
}

export default BlogPost;
