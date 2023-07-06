import { Card } from "react-bootstrap";
import { BsFacebook, BsDiscord, BsInstagram } from "react-icons/bs";

function ProfilAbout() {
  return (
    <>
      <Card className="my-3 p-3 ">
        <Card.Title>Current reading</Card.Title>
        <Card.Img src="https://picsum.photos/91/139" />
      </Card>
      <Card className="my-3 p-3 ">
        <Card.Body>
          <Card.Title>About</Card.Title>
          <br></br>
          <Card.Text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </Card.Text>
          <hr />
          <Card.Text>
            <div style={{ display: "flex", gap: "1.2rem", justifyContent:"center" }}>
              <BsFacebook
                color="#3c5998"
                style={{ width: "2rem", height: "2rem" }}
              />
              <BsInstagram
                color="#FF5701"
                style={{ width: "2rem", height: "2rem" }}
              />
              <BsDiscord
                color="#7189DA"
                style={{ width: "2rem", height: "2rem" }}
              />
            </div>
          </Card.Text>
        </Card.Body>
      </Card>
    </>
  );
}

export default ProfilAbout;
