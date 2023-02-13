import { render } from '@testing-library/react';

import HomeView from './home-view';

describe('HomeView', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<HomeView />);
    expect(baseElement).toBeTruthy();
  });
});
