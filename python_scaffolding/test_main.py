import pytest
from unittest.mock import patch, Mock
from main import fetch_price


@patch("main.requests.get")
def test_fetch_price_success(mock_get):
    # Simulate successful response from Google Finance
    html = """
    <html>
        <body>
            <div class="YMlKec fxKbKc">$123.45</div>
        </body>
    </html>
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = html
    mock_get.return_value = mock_response

    # Capture printed output
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    fetch_price()

    sys.stdout = sys.__stdout__  # Reset stdout
    output = captured_output.getvalue()

    assert "Current GOOG Stock Price: $123.45" in output
