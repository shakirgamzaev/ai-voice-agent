BEGIN;

-- Running upgrade b8032ad7863d -> 2949a6bb6f2b

CREATE TABLE public.threads (
    id UUID NOT NULL, 
    customer_user_id UUID NOT NULL, 
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(customer_user_id) REFERENCES public.customer_user (id)
);

CREATE INDEX ix_public_threads_customer_user_id ON public.threads (customer_user_id);

CREATE TABLE public.messages (
    id UUID NOT NULL, 
    thread_id UUID NOT NULL, 
    role TEXT NOT NULL, 
    text TEXT NOT NULL, 
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    reply_to_message_id UUID, 
    PRIMARY KEY (id), 
    CONSTRAINT ck_messages_role CHECK (role IN ('user', 'assistant')), 
    FOREIGN KEY(reply_to_message_id) REFERENCES public.messages (id), 
    FOREIGN KEY(thread_id) REFERENCES public.threads (id)
);

CREATE INDEX ix_public_messages_thread_id ON public.messages (thread_id);

UPDATE public.alembic_version SET version_num='2949a6bb6f2b' WHERE public.alembic_version.version_num = 'b8032ad7863d';

COMMIT;

