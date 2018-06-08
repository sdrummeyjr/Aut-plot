import colors
import functions as func


def main():
    """file name input from user. need root and extension"""
    file_name = input("What is the file name?")

    """Creates Data Frame"""
    df = func.imp_file(file_name)

    """Get the column headers"""
    cols = func.get_col(df)

    """Pivots Data Frame"""
    print(cols)
    pv_value = input("What do you want to set as the pivot's value? ").upper()
    print(cols)
    pv_index = input("What do you want to set as the pivot's index? ").upper()
    pivot_df = func.pvt_df(df, pv_value, pv_index)

    """Creates the plot from the pivoted data frame"""
    colors.color_map()
    plot_color = input("What color do you want the plot to be? Please refer to the color list in 'PLOT COLORS'.")
    plt_name = func.plot_name(file_name)
    func.create_plot(pivot_df, plot_color, plt_name)


if __name__ == '__main__':
    main()
