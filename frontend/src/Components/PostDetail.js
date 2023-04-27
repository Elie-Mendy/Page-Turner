import React from "react";
import {
  Row,
  Col,
  ListGroup,
  Button,
} from "react-bootstrap";


function PostDetail({ setterView, post }) {

  return (
    <div>
      <Row>
        <Col md={3}>
          <Button className="btn btn-light my-3" onClick={() => setterView(true)}>Go Back</Button>

        </Col>
        <Col md={9}>
          <ListGroup variant="flush">
            <ListGroup.Item>
              <h1>{post.titre}</h1>
            </ListGroup.Item>
            <ListGroup.Item>{post.description}</ListGroup.Item>
          </ListGroup>
        </Col>
      </Row>
    </div>
  );
}

export default PostDetail;
