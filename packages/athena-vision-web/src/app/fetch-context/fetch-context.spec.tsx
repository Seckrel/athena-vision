import { render } from '@testing-library/react';

import FetchContext from './fetch-context';

describe('FetchContext', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<FetchContext />);
    expect(baseElement).toBeTruthy();
  });
});
