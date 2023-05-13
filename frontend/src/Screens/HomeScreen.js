import { Row, Col } from "react-bootstrap";
import { HomeScreenContextProvider } from "../Context/HomeScreenContext";
import HomepageDropdown from "../Components/HomepageDropdown";
import BookList from "../Components/BookList";

import SearchBar from "../Components/SearchBar";

function HomeScreen() {
    return (
        <HomeScreenContextProvider>
            <Row>
                <Col>
                    <HomepageDropdown />
                </Col>
                <Col>
                    <SearchBar />
                </Col>
            </Row>
            <BookList />
        </HomeScreenContextProvider>
    );
}

export default HomeScreen;
