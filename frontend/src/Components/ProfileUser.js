import {  Row, Col, ListGroup } from "react-bootstrap";
import ProfilAbout from '../Components/ProfilAbout'
import ProfilPost from '../Components/ProfilPost'


const ProfileUser = () => {
  return (
    <Row>
      <Col md={3}>
        <ProfilAbout />
      </Col>
      <Col md={9}>
        <ListGroup variant="flush">
          <ListGroup.Item>
            <ProfilPost />
            <ProfilPost />
            <ProfilPost />
            <ProfilPost />
            <ProfilPost />
            <ProfilPost />
          </ListGroup.Item>
        </ListGroup>
      </Col>
    </Row>
  );
};

export default ProfileUser;
