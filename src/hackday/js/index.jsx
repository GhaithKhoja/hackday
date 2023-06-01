import React from "react";
import styled from "@emotion/styled";
import { Colors } from "./components/colors";

class Index extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      placeholder: [],
    };
  }

  // Process when the webpage is called
  componentDidMount() {
    console.log("component mounted");
  };

  render() {
    // This line automatically assigns this.state.imgUrl to the const variable imgUrl
    // and this.state.owner to the const variable owner
    const { users } = this.state;
    // Render index
    return (
      <>
        <h1>Hello World!</h1>
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

