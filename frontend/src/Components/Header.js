import Container from 'react-bootstrap/Container';
import { Nav, Navbar, NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap';
import { useDispatch, useSelector } from 'react-redux'
import { logout } from "../actions/userActions";



function Header() {

  //get the userLogin info 
  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin

  const dispatch = useDispatch()

  const logOutHandler = () => {
    dispatch(logout())
    // TODO - nativate to login page 
  }

  return (
    <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
      <Container>
        <LinkContainer to="/">
          <Navbar.Brand>Page Turner</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="mr-auto"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            {/* <LinkContainer to="/cart">
              <Nav.Link><i className="fas fa-shopping-cart" /> Cart</Nav.Link>
            </LinkContainer> */}
            { userInfo ? (
              <NavDropdown title={userInfo.name} id='username'>
                <LinkContainer to='/profile'>
                  <NavDropdown.Item>Profile</NavDropdown.Item>
                </LinkContainer>
                <NavDropdown.Item onClick={logOutHandler}>Logout</NavDropdown.Item>
              </NavDropdown>
            ):(
              <LinkContainer to="/login">
                <Nav.Link ><i className="fas fa-user" /> Login</Nav.Link>
              </LinkContainer>
            )}
            
          </Nav>
          {/* <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
            />
            <Button variant="outline-success">Search</Button>
          </Form> */}
        </Navbar.Collapse>
      </Container >
    </Navbar >
  );
}

export default Header;