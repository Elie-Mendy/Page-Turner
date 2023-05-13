import { useEffect } from "react";
import { Card } from "react-bootstrap";
import Rating from "./Rating";
import { Link } from "react-router-dom";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { getCoverFromIsbn } from "../actions/bookActions";

function Book({ book }) {
    const dispatch = useDispatch();
    const volumeInfo = book.volumeInfo;
    const saleInfo = book.saleInfo;

    const isbn_10 =
        volumeInfo.industryIdentifiers &&
        volumeInfo.industryIdentifiers[0].identifier;
    const isbn_13 =
        volumeInfo.industryIdentifiers &&
        volumeInfo.industryIdentifiers.length > 1
            ? volumeInfo.industryIdentifiers[1].identifier
            : null;
    const isbn = isbn_13 ? isbn_13 : isbn_10;
    const title = volumeInfo.title;
    const googleCover =
        volumeInfo &&
        volumeInfo.imageLinks &&
        volumeInfo.imageLinks.thumbnail &&
        volumeInfo.imageLinks.thumbnail;

    const img = `https://covers.openlibrary.org/b/isbn/${isbn_13}-M.jpg`;

    const bookCover = useSelector((state) => state.bookCover);
    const { isCover } = bookCover;

    const price = saleInfo.listPrice && saleInfo.listPrice.amount;

    useEffect(() => {
        dispatch(getCoverFromIsbn(isbn_13));
    }, [dispatch]);

    return (
        <Card className="my-3 p-3">
            <Link to={`/books/${isbn}`}>
                <Card.Img src={isCover ? img : googleCover} />
            </Link>

            <Card.Body>
                <Link to={`/books/${isbn}`}>
                    <Card.Title as="div">
                        <strong>{title}</strong>
                    </Card.Title>
                </Link>
            </Card.Body>
            <Card.Text as="div">
                <div className="my-3">
                    <Rating
                        value={4} // TODO Ratin model
                        text={`${56} reviews`}
                        color={"#f8e825"}
                    />
                </div>
            </Card.Text>
            {/* { price && (
                <Card.Text as="h3">
                    {price}
                </Card.Text>
            )} */}
        </Card>
    );
}

export default Book;
