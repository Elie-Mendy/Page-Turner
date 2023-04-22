import { Card } from "react-bootstrap";

function ProfilAbout() {
    return (
        <>
            <Card className="my-3 p-3 ">
                <Card.Title>Lecture en cours</Card.Title>
                <Card.Img src="https://picsum.photos/91/139" />
            </Card>
            <Card className="my-3 p-3 ">
                <Card.Body>
                    <Card.Title>About</Card.Title>
                    <Card.Text>
                        Description de la carte.
                    </Card.Text>
                    <hr/>
                    <Card.Text>
                        Description de la carte. 
                    </Card.Text>
                    <hr/>
                    <Card.Text>
                        Description de la carte. 
                    </Card.Text>
                </Card.Body>
            </Card>
        </>
    );
}

export default ProfilAbout;
