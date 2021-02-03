FROM python:3.7-slim-buster

# Create a working directory.
RUN mkdir wd
WORKDIR wd

# Install Python dependencies.
COPY requirements.txt .
ADD https://files.pythonhosted.org/packages/67/a7/12261a51ac2e7be4c698ca27cbe364ca5f16d64999456ee47ea8c7b44417/pandas-0.23.4-cp37-cp37m-manylinux1_x86_64.whl .
ADD https://github.com/nmalkin/plot-likert.git .
RUN pip3 install pandas-0.23.4-cp37-cp37m-manylinux1_x86_64.whl
RUN pip3 install -r requirements.txt

# Copy the rest of the codebase into the image
COPY . ./

EXPOSE 8000

# Finally, run gunicorn.
# CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "app:server"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 2 --timeout 0 app:server
