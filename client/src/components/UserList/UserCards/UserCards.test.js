import React from "react";
import { shallow } from "enzyme";
import UserCards from "./UserCards";

describe("UserCards", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<UserCards />);
    expect(wrapper).toMatchSnapshot();
  });
});
