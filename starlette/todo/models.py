import sqlalchemy

metadata = sqlalchemy.MetaData()

todo = sqlalchemy.Table(
    "todo",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("created_on", sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column("modified_on", sqlalchemy.DateTime(timezone=True), nullable=True),
    sqlalchemy.Column(
        "author_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id"),
        nullable=False,
    ),
)
