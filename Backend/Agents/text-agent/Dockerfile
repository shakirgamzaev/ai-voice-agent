FROM public.ecr.aws/lambda/python:3.15 AS lambda-base

FROM lambda-base AS dependencies
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /bin/uv
ENV UV_PYTHON_DOWNLOADS=never
WORKDIR /build
COPY pyproject.toml uv.lock README.md ./

# Install only the locked runtime packages using the Lambda interpreter.
RUN uv export --locked --no-dev --no-emit-project --output-file requirements.txt \
    && uv pip install --python /var/lang/bin/python3.15 \
        --no-cache --no-deps --require-hashes \
        --target "${LAMBDA_TASK_ROOT}" --requirements requirements.txt

FROM lambda-base
COPY --from=dependencies ${LAMBDA_TASK_ROOT}/ ${LAMBDA_TASK_ROOT}/
COPY main.py ${LAMBDA_TASK_ROOT}/
CMD ["main.lambda_handler"]
