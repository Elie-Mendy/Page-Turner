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

  const postComment = async () => {
    setErrorBadComment("");
    try {
      if (!userInfo) {
        setErrorBadComment("You must be connected to post a comment");
        return;
      }

      const { data } = await axios.post(`http://127.0.0.1:8000/comments/`, {
        content: commentInputValue,
        isbn: isbn,
        user: { id: userInfo.id },
      });
      fetchData();
      if (data.toxic > 0.5) {
        let message = "This comment is toxic, you're not allowed to post it";  
        setErrorBadComment(message);
      }
      setCommentInputValue("");
    } catch (error) {
      if (!commentInputValue) {
        setErrorBadComment("It's impossible to leave an empty comment");
      } else {
        setErrorBadComment("An error occured while posting your comment");
      }
    }
  };

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/comments/${isbn}`
      );
      setCommentList(response.data);
      setLoading(false);
    } catch (error) {
      setErrorFetchData("Erreur pour récupérer la donnée");
      setLoading(false);
    }
  };

  const deleteComment = async (commentId) => {
    try {
      const response = await axios.patch(`http://127.0.0.1:8000/comments/`, {
        id: commentId,
      });
      fetchData();
    } catch (error) {
      alert("erreur de suppression", error);
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
          <h3>Comments</h3>
          <div className="row">
            {commentList.length === 0 && (
              <div className="col-md-12">
                <Card
                  
                  style={{
                    width: "100%",
                    maxwidth: "500px",
                    marginBottom: "1.5rem",
                  }}
                >
                  <div>
                    <Card.Body>
                      <Card.Text>
                        No comment yet, be the first to comment
                      </Card.Text>
                    </Card.Body>
                  </div>
                </Card>
              </div>
            )

                  }
            {commentList.map((comment) => {
              if (!comment.deleted_at) {
                return (
                  <div key={comment.id} className="col-md-12">
                    <Card
                      style={{
                        width: "100%",
                        maxwidth: "500px",
                        marginBottom: "1.5rem",
                      }}
                    >
                      <div className="row">
                        <div className="col-12">
                          <Card.Header style={{ backgroundColor: "white" }}>
                            <div className="d-flex align-items-center">
                              <Card.Img
                                style={{ width: "6rem", marginRight: "1.5rem" }}
                                variant="top"
                                src="https://i.pinimg.com/564x/0d/64/98/0d64989794b1a4c9d89bff571d3d5842.jpg"
                              />
                              <div>
                                <Card.Title>{comment.user_fullname}</Card.Title>
                                <Card.Subtitle className="mb-2 text-muted">
                                  {moment(comment.created_at)
                                    .local()
                                    .format("YYYY-MM-DD HH:mm")}
                                </Card.Subtitle>
                              </div>
                              <div
                                type="button"
                                className="btn btn-light justify-self-end rounded-circle"
                                variant="outline-secondary"
                                onClick={() => deleteComment(comment.id)}
                              >
                                <RxCross2 />
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
                );
              }
            })}
          </div>
          <h3>Enter a comment</h3>
          <Card
            style={{
              width: "100%",
              maxwidth: "500px",
              marginBottom: "1.5rem",
            }}
          >
            <div>
              <Card.Body>
                <div className="form-floating">
                  <textarea
                    className="form-control"
                    placeholder="Leave a comment here"
                    id="floatingTextarea2"
                    style={{ height: "100px" }}
                    value={commentInputValue}
                    onChange={(e) => setCommentInputValue(e.target.value)}
                  ></textarea>
                  <label className="floatingTextarea2">Leave your comment there 😃</label>
                  <button
                    type="button"
                    className="btn btn-light mt-4"
                    onClick={postComment}
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
