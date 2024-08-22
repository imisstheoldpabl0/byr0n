import React from "react";
import { shallow } from "enzyme";
import UserTopComp from "./UserTopComp";

describe("UserTopComp", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<UserTopComp />);
    expect(wrapper).toMatchSnapshot();
  });
});
