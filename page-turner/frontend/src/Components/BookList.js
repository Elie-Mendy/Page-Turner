import { useContext } from "react";
import { HomeScreenContext } from "../Context/HomeScreenContext";
import { Row, Col, Container } from "react-bootstrap";
import Book from "../Components/Book";
import Loader from "../Components/Loader";
import Message from "../Components/Message";

function BookList() {
    const { loading, error, books, searchType } = useContext(HomeScreenContext);
    console.log("error ", error)
    return (
        <Container className="text-center py-3">
            {loading && <Loader />}
            {error && <Message variant="danger">{error}</Message>}
            {books && books.items ? searchType === "tab3" ? (
                <>
                    <h2>Vos livres préférés</h2>
                    <Row>
                        {books.items.slice(0, 4).map((book) => (
                            <Col key={book.id} sm={12} md={6} lg={3}>
                                <Book book={book} />
                            </Col>
                        ))}
                    </Row>
                    <h2>Recommandations</h2>
                    <Row>
                        {books.items.slice(4).map((book) => (
                            <Col key={book.id} sm={12} md={6} lg={3}>
                                <Book book={book} />
                            </Col>
                        ))}
                    </Row>
                </>
            ) : (
                <Row>
                    {books.items.map((book) => (
                        <Col key={book.id} sm={12} md={6} lg={3}>
                            <Book book={book} />
                        </Col>
                    ))}
                </Row>
            ) : null}
        </Container>
    );
}

export default BookList;