import Container from "react-bootstrap/Container";
import { Nav, Navbar, NavDropdown } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../Actions/userActions";

function Header() {
    //get the userLogin info
    const userLogin = useSelector((state) => state.userLogin);
    const { userInfo } = userLogin;

    const dispatch = useDispatch();

    const logOutHandler = () => {
        dispatch(logout());
        // TODO - nativate to login page
    };

    return (
        <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
            <Container className='d-flex justify-content-between'>
                <LinkContainer to="/">
                    <Navbar.Brand>Page Turner</Navbar.Brand>
                </LinkContainer>
                <Navbar.Toggle aria-controls="navbarScroll" />
                <Navbar.Collapse className="justify-content-end" id="navbarScroll">
                    <Nav
                        className="mr-auto"
                        style={{ maxHeight: "100px"}}
                        navbarScroll
                    >
                        {/* <LinkContainer to="/cart">
              <Nav.Link><i className="fas fa-shopping-cart" /> Cart</Nav.Link>
            </LinkContainer> */}
                        {userInfo ? (
                            <NavDropdown title={userInfo.name} id="username">
                                <LinkContainer to="/profile">
                                    <NavDropdown.Item>Profil</NavDropdown.Item>
                                </LinkContainer>
                                <LinkContainer to="/infos-profile">
                                    <NavDropdown.Item>Informations</NavDropdown.Item>
                                </LinkContainer>
                                <NavDropdown.Item onClick={logOutHandler}>
                                    Se déconnecter
                                </NavDropdown.Item>
                            </NavDropdown>
                        ) : (
                            <LinkContainer to="/login">
                                <Nav.Link>
                                    <i className="fas fa-user" /> Login
                                </Nav.Link>
                            </LinkContainer>
                        )}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default Header;
