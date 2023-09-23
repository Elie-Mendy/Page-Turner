import { Row, Col, Button} from "react-bootstrap";
import { HomeScreenContextProvider } from "../Context/HomeScreenContext";
import HomepageDropdown from "../Components/HomepageDropdown";
import BookList from "../Components/BookList";

import SearchBar from "../Components/SearchBar";
import SearchButton from "../Components/SearchButton";

function HomeScreen() {
    return (
        <HomeScreenContextProvider>
            <Row>
                <Col>
                    <HomepageDropdown />
                </Col>
                <Col className="homepage-search">
                    <SearchBar />
                    <SearchButton/>
                </Col>
            </Row>
            <BookList />
        </HomeScreenContextProvider>
    );
}

export default HomeScreen;
