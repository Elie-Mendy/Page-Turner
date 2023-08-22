import React, { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { Row, Col, Image, ListGroup, Card } from "react-bootstrap";
import Rating from "../Components/Rating";

import { useDispatch, useSelector } from "react-redux";
import { listBooksDetails, getCoverFromIsbn } from "../Actions/bookActions";

import Loader from "../Components/Loader";
import Message from "../Components/Message";
import Comment from "../Components/Comment";

function BookScreen() {
    const match = useParams();
    const dispatch = useDispatch();
    //const img = `https://covers.openlibrary.org/b/isbn/${match.isbn}-M.jpg`
    const img = `http://images.amazon.com/images/P/${match.isbn}.01.LZZZZZZZ.jpg`;

    const bookDetail = useSelector((state) => state.bookDetail);
    const { error, loading, book } = bookDetail;
    const volumeInfo = book.volumeInfo;
    const averageRating = volumeInfo && volumeInfo.averageRating;
    const ratingsCount = volumeInfo && volumeInfo.ratingsCount;

    const bookCover = useSelector((state) => state.bookCover);
    const { isCover } = bookCover;
    const not_found_url = "https://pick2read.com/assets/images/not_found.png";

    useEffect(() => {
        dispatch(listBooksDetails(match.isbn));
        dispatch(getCoverFromIsbn(match.isbn));
    }, [dispatch, match]);

    return (
        <div>
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
                                              book.volumeInfo.imageLinks
                                            ? book.volumeInfo.imageLinks
                                                  .thumbnail
                                            : not_found_url
                                    }
                                    alt={book.name}
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
                                        value={averageRating}
                                        text={`${ratingsCount} reviews`}
                                        color={"#f8e825"}
                                    />
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
            <Comment isbn={match.isbn} />
        </div>
    );
}

export default BookScreen;
