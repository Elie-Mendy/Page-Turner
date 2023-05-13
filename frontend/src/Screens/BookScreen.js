import React, { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { Row, Col, Image, ListGroup, Card } from "react-bootstrap";
import Rating from "../Components/Rating";

import { useDispatch, useSelector } from "react-redux";
import { listBooksDetails, getCoverFromIsbn } from "../Actions/bookActions";

import Loader from "../Components/Loader";
import Message from "../Components/Message";

function BookScreen() {
    const match = useParams();
    const dispatch = useDispatch();
    //const img = `https://covers.openlibrary.org/b/isbn/${match.isbn}-M.jpg`
    const img = `http://images.amazon.com/images/P/${match.isbn}.01.LZZZZZZZ.jpg`;

    const bookDetail = useSelector((state) => state.bookDetail);
    const { error, loading, book } = bookDetail;

    const bookCover = useSelector((state) => state.bookCover);
    const { isCover } = bookCover;

    useEffect(() => {
        console.log("useEffect", match.isbn);
        dispatch(listBooksDetails(match.isbn));
        dispatch(getCoverFromIsbn(match.isbn));
    }, [dispatch, match]);

    return (
        <div>
            <Link to="/" className="btn btn-light my-3">
                Go Back
            </Link>
            {loading ? (
                <Loader />
            ) : error ? (
                <Message variant="danger">{error}</Message>
            ) : (
                book && (
                    <Row>
                        <Col md={4}>
                            <Image />
                            <Card className="my-3 p-3 ">
                                <Card.Img
                                    src={
                                        isCover
                                            ? img
                                            : book &&
                                              book.volumeInfo &&
                                              book.volumeInfo.imageLinks &&
                                              book.volumeInfo.imageLinks
                                                  .thumbnail
                                    }
                                    alt={book.name}
                                    fluid
                                />
                            </Card>
                        </Col>
                        <Col md={8}>
                            <ListGroup variant="flush">
                                <ListGroup.Item>
                                    <h3>{book.name}</h3>
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Rating
                                        value={book.rating}
                                        text={`${book.numReviews} reviews`}
                                        color={"#f8e825"}
                                    />
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    Price: ${book.price}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    Description:{" "}
                                    {book.volumeInfo &&
                                        book.volumeInfo.description}
                                </ListGroup.Item>
                            </ListGroup>
                        </Col>
                    </Row>
                )
            )}
        </div>
    );
}

export default BookScreen;
