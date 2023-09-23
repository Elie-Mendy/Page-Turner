import { useState, useEffect } from "react";
import axios from "axios";
import { Card } from "react-bootstrap";
import Rating from "./Rating";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";

function Book({ book }) {
  const dispatch = useDispatch();
  const volumeInfo = book.volumeInfo;
  const isbn_10 =
    volumeInfo.industryIdentifiers &&
    volumeInfo.industryIdentifiers[0].identifier;
  const isbn_13 =
    volumeInfo.industryIdentifiers && volumeInfo.industryIdentifiers.length > 1
      ? volumeInfo.industryIdentifiers[1].identifier
      : null;
  const isbn = isbn_13 ? isbn_13 : isbn_10;
  const title = volumeInfo.title;
  const googleCover =
    volumeInfo &&
    volumeInfo.imageLinks &&
    volumeInfo.imageLinks.thumbnail &&
    volumeInfo.imageLinks.thumbnail;

  const [cover, setCover] = useState(googleCover);

  const averageRating = volumeInfo && volumeInfo.averageRating;
  const ratingsCount = volumeInfo && volumeInfo.ratingsCount;

  async function getCoverFromIsbn(isbn) {
    let coverAmazon = new Image();
    let coverUrl = `http://images.amazon.com/images/P/${isbn}.01.LZZZZZZZ.jpg`;
    coverAmazon = await axios.get(coverUrl);
    if (
      coverAmazon.data !==
      "GIF89a\u0001\u0000\u0001\u0000�\u0001\u0000\u0000\u0000\u0000���!�\u0004\u0001\u0000\u0000\u0001\u0000,\u0000\u0000\u0000\u0000\u0001\u0000\u0001\u0000\u0000\u0002\u0002L\u0001\u0000;"
    ) {
      setCover(coverUrl);
    }
    if (!cover) {
      setCover("https://pick2read.com/assets/images/not_found.png");
    }
  }

  //const img = `https://covers.openlibrary.org/b/isbn/${isbn_13}-M.jpg`;

  useEffect(() => {
    getCoverFromIsbn(isbn);
  }, [isbn]);

  return (
    <Card className="my-3 p-3">
      <Link to={`/books/${isbn}`} target="_blank">
        <Card.Img src={cover} />
      </Link>

      <Card.Body>
        <Link to={`/books/${isbn}`} target="_blank">
          <Card.Title as="div">
            <strong>{title}</strong>
          </Card.Title>
        </Link>
      </Card.Body>
      <Card.Text as="div">
        <div className="my-3">
          <Rating
            value={averageRating}
            text={`${ratingsCount} reviews`}
            color={"#f8e825"}
          />
        </div>
      </Card.Text>
    </Card>
  );
}

export default Book;