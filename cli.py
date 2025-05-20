from rmp.main import main, get_parser

if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args)
