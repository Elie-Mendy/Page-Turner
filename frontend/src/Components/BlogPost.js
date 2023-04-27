import {
  Row,
  Col,
} from "react-bootstrap";
import posts from "../posts";
import PostCard from "./PostCard";
import PostDetail from './PostDetail';
import { useState } from "react";


function BlogPost() {
  const [gridView, setGridView] = useState(true);
  const [postId, setpostId] = useState(1);

  return (
    <Row>
      {gridView ? posts.map((post, index) => (
        <Col key={index} sm={12} md={6} lg={3}>
          <PostCard post={post} setterView={setGridView} setterPostId={setpostId}/>
        </Col>
      )) : <PostDetail post={posts[postId - 1]} setterView={setGridView}/>}
    </Row>
  );
}

export default BlogPost;
