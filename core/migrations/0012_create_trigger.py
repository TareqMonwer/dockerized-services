# Generated by Django 4.0.3 on 2022-04-26 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_millionaire_core_millio_name_b48509_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                CREATE TRIGGER vector_column_trigger
                BEFORE INSERT OR UPDATE OF name, profession, vector_column
                ON millionaire
                FOR EACH ROW EXECUTE PROCEDURE
                tsvector_update_trigger(
                    vector_column, 'pg_catalog.english', name, profession
                );

                UPDATE millionaire SET vector_column = NULL;
                ''',

            reverse_sql = '''
                DROP TRIGGER IF EXISTS vector_column_trigger
                ON millionaire;'''
        ),
    ]
