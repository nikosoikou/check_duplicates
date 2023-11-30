import logging


def check_duplicates(df, cols):
    """
    This function checks for duplicates in a dataframe, based on the columns
    specified.

    Parameters:
    df (pandas.DataFrame): The input dataframe.
    cols (list): A list of columns on which the dataframe should be checked
                 for duplicates.

    Returns:
    dict: A dictionary containing the following items:
          - count: number of cases where duplicates occur.
          - samples: dataframe with group count of duplicate rows for the
                     columns from the input, e.g.:
                         col_1, col_2, number_of_duplicates
    """
    try:
        # Find duplicates
        duplicates = df[df.duplicated(subset=cols, keep=False)]

        # Count duplicates
        count = len(duplicates)

        # Group by columns and count duplicates
        samples = duplicates\
            .groupby(cols)\
            .size()\
            .reset_index(name='number_of_duplicates')

        # Return dictionary
        return {'count': count, 'samples': samples}

    except Exception as e:
        logging.error(f"Error in check_duplicates: {e}")

        raise e
