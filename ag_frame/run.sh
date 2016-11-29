#!/usr/bin/env bash


run (){
    if [[ $# -lt 2 ]]; then
        echo "Not enought args!"
        echo "<alg_name> <function_name> "
        exit
    fi

    echo "---- With 5"
    ag_frame "$1" -p 8 -m 50 "$2" -d 5 > "$1"_"$2"_5_RMHC.csv
    echo "---- With 10"
    ag_frame "$1" -p 8 -m 50 "$2" -d 10 > "$1"_"$2"_10_RMHC.csv
    echo "---- With 30"
    ag_frame "$1" -p 8 -m 50 "$2" -d 30 > "$1"_"$2"_30_RMHC.csv
}

algs=(random_mutation_hill_climbing next_ascent_hill_climbing steepest_ascent_hill_climbing simulated_annealing)
funcs=(griewangks_function rastrigins_function rosenbrocks_valley)

cd out_directory
for alg in ${algs[@]}; do
    for func in ${funcs[@]}; do
        echo "Running $alg with $func"
        run "$alg" "$func"
    done
done

# special case for six-hump_camel_back
f="six-hump_camel_back"
for alg in ${algs[@]}; do
    echo "Running $alg with $f"
    echo "---- With 5"
    ag_frame "$alg" -p 8 -m 50 "$f" > "$alg"_"$f"_5_RMHC.csv
    echo "---- With 10"
    ag_frame "$alg" -p 8 -m 50 "$f" > "$alg"_"$f"_10_RMHC.csv
    echo "---- With 30"
    ag_frame "$alg" -p 8 -m 50 "$f" > "$alg"_"$f"_30_RMHC.csv
done
