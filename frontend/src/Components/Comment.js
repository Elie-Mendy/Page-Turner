import React, { useEffect, useState } from "react";
import { Button, Card } from "react-bootstrap";
import axios from "axios";
import Loader from "../Components/Loader";
import Message from "../Components/Message";
import moment from "moment";
import { useSelector } from "react-redux";
import Alert from "react-bootstrap/Alert";
import { RxCross2 } from "react-icons/rx";

function Comment({ isbn }) {
  const [commentList, setCommentList] = useState(null);
  const [loading, setLoading] = useState(true);
  const [errorFetchData, setErrorFetchData] = useState("");
  const [errorBadComment, setErrorBadComment] = useState("");
  const [commentInputValue, setCommentInputValue] = useState("");

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  const handleClick = async () => {
    console.log("ID DE MON USER ==>", userInfo.id);
    setErrorBadComment("");
    try {
      const response = await axios.post(`http://127.0.0.1:8000/comments/`, {
        content: commentInputValue,
        isbn: isbn,
        user: { id: userInfo.id },
      });
      fetchData();
      console.log(response);
      setCommentInputValue("");
    } catch (error) {
      if (!commentInputValue) {
        setErrorBadComment("Ce commentaire est vide");
      } else {
        setErrorBadComment("Ce commentaire contient 'gros_mot'");
      }
    }
  };

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/comments/${isbn}`
      );
      setCommentList(response.data);
      console.log(response.data);
      setLoading(false);
    } catch (error) {
      setErrorFetchData("Erreur pour récupérer la donnée");
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      {loading && <Loader />}
      {errorFetchData && <Message variant="danger">{errorFetchData}</Message>}
      {commentList && (
        <Card style={{ backgroundColor: "#d4d4d4", boxShadow: "2px" }}>
          <h3>COMMENTAIRES</h3>
          <div className="row">
            {commentList.map((comment) => (
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
                      <Button variant="outline-secondary">
                        <RxCross2 />
                      </Button>
                      <Card.Header style={{ backgroundColor: "white" }}>
                        <div class="d-flex align-items-center">
                          <Card.Img
                            style={{ width: "6rem", marginRight: "1.5rem" }}
                            variant="top"
                            src="https://i.pinimg.com/564x/0d/64/98/0d64989794b1a4c9d89bff571d3d5842.jpg"
                          />
                          <div>
                            <Card.Title>Fake it</Card.Title>
                            <Card.Subtitle className="mb-2 text-muted">
                              {moment(comment.created_at)
                                .local()
                                .format("YYYY-MM-DD HH:mm")}
                            </Card.Subtitle>
                          </div>
                        </div>
                      </Card.Header>
                    </div>
                  </div>
                  <div>
                    <Card.Body>
                      <Card.Text>{comment.content}</Card.Text>
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
            <div>
              <Card.Body>
                <div class="form-floating">
                  <textarea
                    class="form-control"
                    placeholder="Leave a comment here"
                    id="floatingTextarea2"
                    style={{ height: "100px" }}
                    value={commentInputValue}
                    onChange={(e) => setCommentInputValue(e.target.value)}
                  ></textarea>
                  <label for="floatingTextarea2">Votre commentaire</label>
                  <button
                    type="button"
                    class="btn btn-light mt-4"
                    onClick={handleClick}
                  >
                    Poster
                  </button>
                  {errorBadComment && (
                    <Alert variant="danger">{errorBadComment}</Alert>
                  )}
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
