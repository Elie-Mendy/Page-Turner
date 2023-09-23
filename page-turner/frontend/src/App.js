import { Container } from "react-bootstrap";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import HomeScreen from "./Screens/HomeScreen";
import BookScreen from "./Screens/BookScreen";
import LoginScreen from "./Screens/LoginScreen";
import RegisterScreen from "./Screens/RegisterScreen";
import ProfileScreen from "./Screens/ProfileScreen";
import InfoScreen from "./Screens/InfoScreen";


 
function App() {
  return (
    <BrowserRouter>
      <Header />
      <main className="py-3">
        <Container>
          <Routes>
            <Route path="/" element={<HomeScreen />} exact/>
            <Route path="/login" element={<LoginScreen />} exact/>
            <Route path="/register" element={<RegisterScreen />} exact/>
            <Route path="/profile" element={<ProfileScreen />} exact/>
            <Route path="/infos-profile" element={<InfoScreen />} exact/>
            <Route path="/books/:isbn" element={<BookScreen />} />
          </Routes>
        </Container>
      </main>
      <Footer />
    </BrowserRouter>
  );
}
 
export default App;