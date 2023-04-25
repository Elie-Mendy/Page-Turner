import { Row, Col, Image, ListGroup, Button, Card, Form } from 'react-bootstrap'

function BlogPost() {
    return (
        <ListGroup variant="flush">
          <Row>
            <Col md={4}>
            <ListGroup.Item>
                <strong>Premier article de blog ! </strong>
                <br/>
                <br/>
                Lorem ipsum dolor sit amet, consectetur 
                adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </ListGroup.Item>
            </Col>
            <Col md={4}>
              <ListGroup.Item>
                  <strong>Deuxième article de blog ! </strong>
                  <br/>
                  <br/>
                  Lorem ipsum dolor sit amet, consectetur 
                  adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </ListGroup.Item>
            </Col>
            <Col md={4}>
              <ListGroup.Item>
                  <strong>Troisième article de blog !</strong>
                  <br/>
                  <br/>
                  Lorem ipsum dolor sit amet, consectetur 
                  adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </ListGroup.Item> 
            </Col>
          </Row>
        </ListGroup>
    );
}

export default BlogPost;
