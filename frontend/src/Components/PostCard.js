import { Card } from "react-bootstrap";


function PostCard({ post, setterView, setterPostId }) {
  const handleClick = () => {
    setterPostId(post.id);
    setterView(false);
  };

  return (
    <Card className="my-3 p-3" onClick={() => handleClick()}>
      <Card.Body>
        <Card.Title as="div">{post.titre}</Card.Title>
      </Card.Body>
      <Card.Text as="div">
        <div className="my-3">{post.description.substring(0, 255) + "..."}</div>
      </Card.Text>
    </Card>
  );
}

export default PostCard;
