import { useContext } from "react";
import { HomeScreenContext } from "../Context/HomeScreenContext";
import { Row, Col, Container } from "react-bootstrap";
import Book from "../Components/Book";
import Loader from "../Components/Loader";
import Message from "../Components/Message";

function BookList() {
    const { loading, error, books } = useContext(HomeScreenContext);

    return (
        <Container className="text-center py-3">
            {loading && <Loader/>}
            {error && <Message variant="danger">{error}</Message>}
            {books && books.items && (
                <Row>
                    {books.items.map((book) => (
                        <Col key={book.id} sm={12} md={6} lg={3}>
                            <Book book={book} />
                        </Col>
                    ))}
                </Row>
            )}
        </Container>
    );
}

export default BookList;
