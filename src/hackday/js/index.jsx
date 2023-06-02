import React from "react";
import styled from "@emotion/styled";
import Button from "@mui/material/Button";
import { Colors } from "./components/colors";
import { TextField } from "@mui/material";

class Index extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      forkedSet: false,
      forkedValue: false,
      username: "",
      searched: false,
      repoCount: 0,
      stargazeCount: 0,
      forkCount: 0,
      avgSize: "",
      langList: []
    };
    // bind
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handleSearchSubmit = this.handleSearchSubmit.bind(this);
  }

  // Handle search submit request
  handleSearchSubmit = () => {
    fetch(`/api/v1/search/?username=${this.state.username}`, { credentials: "same-origin", method: "GET" })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          repoCount: data.total_repo_count,
          stargazeCount: data.total_stargazers,
          forkCount: data.total_fork_count,
          avgSize: data.avg_repo_size,
          langList: data.language_list,
          searched: true
        });
      })
      .catch((error) => console.log(error));
      // Handle websocket
  }

  // Handle username request
  handleUsernameChange = (event) => {
    this.setState({ username: event.target.value });
  }

  render() {
    // This line automatically assigns this.state.imgUrl to the const variable imgUrl
    // and this.state.owner to the const variable owner
    const { 
      forkedSet,
      forkedValue,
      username,
      searched,
      repoCount,
      stargazeCount,
      forkCount,
      avgSize,
      langList,
      } = this.state;
    // Render index
    return (
      <>
        <Col>
          <Header>
            <span>Ghaith's <SambosaColor>Github Stats</SambosaColor> Lookup</span>
          </Header>
          <OrderSpan>Input Username!</OrderSpan>
          <InputText
                      required
                      id="filled-required"
                      label="Username"
                      variant="filled"
                      value={username}
                      onChange={this.handleUsernameChange}
                    />
          <SubmitButton
            onClick={() => {this.handleSearchSubmit(); this.handleSearchSubmit();}}
          >
            Submit
          </SubmitButton>
          {searched ? (
            <>
              <OrderSpan>Total repo count: {repoCount}</OrderSpan>
              <OrderSpan>Total stargaze count: {stargazeCount}</OrderSpan>
              <OrderSpan>Total fork count: {forkCount}</OrderSpan>
              <OrderSpan>Avg repo size: {avgSize}</OrderSpan>
              <OrderSpan>Languages used:</OrderSpan>
              {langList.map((item, index) => (
              <OrderSpan key={index}>{item}</OrderSpan>
              ))}
            </>
          ) : (
            <></>
          )}
        </Col>
      </>
    );
  }
}
export default Index;

// Create a flex row display div
const FlexRow = styled.div`
  display: flex;
  flex-direction: row;
`;

// Create a flex column display div
const FlexCol = styled.div`
  display: flex;
  flex-direction: column;
`;


// Create the front page column
const Col = styled(FlexCol)`
  justify-content: center;
  text-align: center;
  align-items: center;
`

// Create a header for the service
const Header = styled(FlexRow)`
  font-size: 36px;
  font-style: italic;
  font-weight: 600;
  justify-content: center;
  align-items: center;
  margin-top: 24vh;
`

// Create a span styling that will display the sambosa count
const SambosaSpan = styled.span`
  margin-top: 12px;
  font-size: 28px;
  font-weight: 600;
`

// Styling for the sambosa icon
const SambosaImg = styled.img`
  width: 64px;
  height: auto;
`

// A span with the sambosa color
const SambosaColor = styled.span`
  color: ${Colors.goLink};
`

// Styled span for the word 'order'
const OrderSpan = styled.span`
  font-size: 36px;
  font-weight: 700;
  margin-top: 16px;
`

// Styled span to tell to track order
const SaveIdSpan = styled.span`
  font-size: 16px;
  font-weight: 700;
  color: ${Colors.brightRed};
`

// Styled row to display service buttons
const ServiceRow = styled(FlexRow)`
  justify-content: center;
  gap: 16px;
  margin-top: 8px;
`

// Create service button
const ServiceButton = styled(Button)(() => ({
  fontSize: "24px",
  fontFamily: "Orbitron",
  fontWeight: "500",
  width: "160px",
  color: Colors.black,
  backgroundColor: Colors.goLink,
  borderRadius: "12px",
  padding: "16px",
  '&:hover': {
    backgroundColor: Colors.darkFried,
    color: Colors.lightFried,
  }
}));

// Create submit button
const SubmitButton = styled(ServiceButton)(() => ({
  marginTop: '24px',
  marginBottom: '24px',
}));

// Create a styled input text field
const InputText = styled(TextField)(() => ({
  width: '40%',
  marginTop: '8px',
}));
