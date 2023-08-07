import React, { useEffect, useState } from "react";
import { Card, InputGroup, Form } from "react-bootstrap";
import axios from "axios";
import Loader from "../Components/Loader";
import Message from "../Components/Message";

const commentData = [
  {
    id: 1,
    pseudo: "User 1",
    date: "01/08/2023",
    commentaire:
      "Commentaire Commentaire Commentaire Commentaire Commentaire 1",
  },
  {
    id: 2,
    pseudo: "User 2",
    date: "02/08/2023",
    commentaire:
      "Commentaire Commentaire Commentaire Commentaire Commentaire 2",
  },
  {
    id: 3,
    pseudo: "User 3",
    date: "03/08/2023",
    commentaire:
      "Commentaire Commentaire Commentaire Commentaire Commentaire 3",
  },
];

function Comment() {
  const [commentList, setCommentList] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const isbn = 9780590353403;

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/comments/${isbn}`
      );
      console.log(response.data);
      setCommentList(response.data);
      setLoading(false);
    } catch (error) {
      setError("Erreur pour récupérer la donnée");
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      {loading && <Loader />}
      {error && <Message variant="danger">{error}</Message>}
      {commentList && (
        <Card style={{ backgroundColor: "#d4d4d4", boxShadow: "2px" }}>
          <h3>COMMENTAIRES</h3>
          <div className="row">
            {commentData.map((comment) => (
              <div key={comment.id} className="col-md-12">
                <Card
                  style={{
                    width: "100%",
                    maxwidth: "500px",
                    marginBottom: "1.5rem",
                  }}
                >
                  <div className="row">
                    <div className="col-4">
                      <Card.Header style={{ backgroundColor: "white" }}>
                        <div class="d-flex align-items-center">
                          <Card.Img
                            style={{ width: "6rem", marginRight: "1.5rem" }}
                            variant="top"
                            src="https://i.pinimg.com/564x/0d/64/98/0d64989794b1a4c9d89bff571d3d5842.jpg"
                          />
                          <div>
                            <Card.Title>{comment.pseudo}</Card.Title>
                            <Card.Subtitle className="mb-2 text-muted">
                              {comment.date}
                            </Card.Subtitle>
                          </div>
                        </div>
                      </Card.Header>
                    </div>
                  </div>
                  <div>
                    <Card.Body>
                      <Card.Text>{comment.commentaire}</Card.Text>
                    </Card.Body>
                  </div>
                </Card>
              </div>
            ))}
          </div>
          <h3>VOTRE COMMENTAIRE</h3>
          <Card
            style={{
              width: "100%",
              maxwidth: "500px",
              marginBottom: "1.5rem",
            }}
          >
            <div className="row">
              <div className="col-4">
                <Card.Header style={{ backgroundColor: "white" }}>
                  <div class="d-flex align-items-center">
                    <Card.Img
                      style={{ width: "6rem", marginRight:"1.5rem" }}
                      variant="top"
                      src="https://i.pinimg.com/564x/0d/64/98/0d64989794b1a4c9d89bff571d3d5842.jpg"
                    />

                    <Card.Title>Pseudo</Card.Title>

                  </div>
                </Card.Header>
              </div>
            </div>
            <div>
              <Card.Body>
                <div class="form-floating">
                  <textarea
                    class="form-control"
                    placeholder="Leave a comment here"
                    id="floatingTextarea2"
                    style={{ height: "100px" }}
                  ></textarea>
                  <label for="floatingTextarea2">Votre commentaire</label>
                </div>
              </Card.Body>
            </div>
          </Card>
        </Card>
      )}
    </>
  );
}

export default Comment;
